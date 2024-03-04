import FWCore.ParameterSet.Config as cms

def SiPixelMonitorTrackResiduals(**kwargs):
  mod = cms.EDProducer('SiPixelMonitorTrackResiduals',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
