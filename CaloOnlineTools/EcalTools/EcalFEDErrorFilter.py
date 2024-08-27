import FWCore.ParameterSet.Config as cms

def EcalFEDErrorFilter(**kwargs):
  mod = cms.EDFilter('EcalFEDErrorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
