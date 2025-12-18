import FWCore.ParameterSet.Config as cms

def HiEgammaSCCorrectionMaker(*args, **kwargs):
  mod = cms.EDProducer('HiEgammaSCCorrectionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
