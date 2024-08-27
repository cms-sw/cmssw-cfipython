import FWCore.ParameterSet.Config as cms

def EcalFEtoDigi(**kwargs):
  mod = cms.EDProducer('EcalFEtoDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
