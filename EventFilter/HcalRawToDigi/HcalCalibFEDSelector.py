import FWCore.ParameterSet.Config as cms

def HcalCalibFEDSelector(**kwargs):
  mod = cms.EDProducer('HcalCalibFEDSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
