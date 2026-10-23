import FWCore.ParameterSet.Config as cms

def EgammaSCCorrectionMaker(*args, **kwargs):
  mod = cms.EDProducer('EgammaSCCorrectionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
