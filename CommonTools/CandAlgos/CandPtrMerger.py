import FWCore.ParameterSet.Config as cms

def CandPtrMerger(**kwargs):
  mod = cms.EDProducer('CandPtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
