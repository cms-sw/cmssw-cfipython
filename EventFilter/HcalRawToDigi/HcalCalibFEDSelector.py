import FWCore.ParameterSet.Config as cms

def HcalCalibFEDSelector(*args, **kwargs):
  mod = cms.EDProducer('HcalCalibFEDSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
