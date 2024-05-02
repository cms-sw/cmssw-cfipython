import FWCore.ParameterSet.Config as cms

def EcalSrFlagColMerger(**kwargs):
  mod = cms.EDProducer('EcalSrFlagColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
