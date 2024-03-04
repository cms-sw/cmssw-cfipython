import FWCore.ParameterSet.Config as cms

def CandFwdPtrMerger(**kwargs):
  mod = cms.EDProducer('CandFwdPtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
