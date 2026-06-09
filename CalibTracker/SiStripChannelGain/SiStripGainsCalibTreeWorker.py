import FWCore.ParameterSet.Config as cms

def SiStripGainsCalibTreeWorker(*args, **kwargs):
  mod = cms.EDProducer('SiStripGainsCalibTreeWorker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
