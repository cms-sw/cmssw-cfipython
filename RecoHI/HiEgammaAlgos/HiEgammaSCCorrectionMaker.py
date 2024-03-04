import FWCore.ParameterSet.Config as cms

def HiEgammaSCCorrectionMaker(**kwargs):
  mod = cms.EDProducer('HiEgammaSCCorrectionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
