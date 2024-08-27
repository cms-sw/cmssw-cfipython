import FWCore.ParameterSet.Config as cms

def SiStripGainsCalibTreeWorker(**kwargs):
  mod = cms.EDProducer('SiStripGainsCalibTreeWorker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
