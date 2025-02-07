import FWCore.ParameterSet.Config as cms

def SiPixelDigiErrorsSoAFromCUDA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelDigiErrorsSoAFromCUDA',
    src = cms.InputTag('siPixelClustersCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
