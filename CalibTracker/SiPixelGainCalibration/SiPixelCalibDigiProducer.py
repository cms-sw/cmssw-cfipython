import FWCore.ParameterSet.Config as cms

def SiPixelCalibDigiProducer(**kwargs):
  mod = cms.EDProducer('SiPixelCalibDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
