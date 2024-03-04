import FWCore.ParameterSet.Config as cms

def SiPixelPhase1TrackEfficiency(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1TrackEfficiency',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
