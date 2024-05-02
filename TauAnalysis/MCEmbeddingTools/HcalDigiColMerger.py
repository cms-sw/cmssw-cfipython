import FWCore.ParameterSet.Config as cms

def HcalDigiColMerger(**kwargs):
  mod = cms.EDProducer('HcalDigiColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
