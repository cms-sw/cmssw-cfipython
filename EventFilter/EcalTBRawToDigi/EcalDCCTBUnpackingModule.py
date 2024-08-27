import FWCore.ParameterSet.Config as cms

def EcalDCCTBUnpackingModule(**kwargs):
  mod = cms.EDProducer('EcalDCCTBUnpackingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
