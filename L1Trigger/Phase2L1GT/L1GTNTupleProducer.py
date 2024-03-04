import FWCore.ParameterSet.Config as cms

def L1GTNTupleProducer(**kwargs):
  mod = cms.EDAnalyzer('L1GTNTupleProducer',
    producerName = cms.required.string,
    maxNTuples = cms.required.uint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
