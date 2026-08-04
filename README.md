# Parche Agent
Agentic data intelligence — ingest structured or unstructured records, 
synthesize insights, and answer questions with citations, evaluation, 
and cost observability.

## Problem
Teams pay for data access but still spend hours manually reading records 
to find patterns. This turns raw records into synthesized, queryable intelligence.

## First use case
Import/competitor intelligence: ingest import records → summarize who is 
importing what, surface trends, answer natural-language questions.

## Roadmap
- [X] Phase 1: Core agent loop (tool selection + memory)
- [X] Phase 2: Retrieval (chunking, embeddings, vector store)
- [ ] Phase 3: FastAPI service (ingest + query endpoints)
- [ ] Phase 4: Evaluation + observability (LLM-as-judge, cost logging)
- [ ] Phase 5: Docker + cloud deploy (live URL)
- [ ] Phase 6: Write-up (design decisions + tradeoffs)

## Tech
Python · FastAPI · [vector store TBD] · Docker · [cloud TBD]