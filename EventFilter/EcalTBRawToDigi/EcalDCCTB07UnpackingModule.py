import FWCore.ParameterSet.Config as cms

def EcalDCCTB07UnpackingModule(**kwargs):
  mod = cms.EDProducer('EcalDCCTB07UnpackingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
