import FWCore.ParameterSet.Config as cms

def EgammaSCCorrectionMaker(**kwargs):
  mod = cms.EDProducer('EgammaSCCorrectionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod