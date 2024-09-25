import FWCore.ParameterSet.Config as cms

def SiPixelDigisSoAFromCUDA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelDigisSoAFromCUDA',
    src = cms.InputTag('siPixelClustersCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
