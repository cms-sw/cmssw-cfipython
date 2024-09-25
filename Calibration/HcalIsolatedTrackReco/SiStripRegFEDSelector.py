import FWCore.ParameterSet.Config as cms

def SiStripRegFEDSelector(*args, **kwargs):
  mod = cms.EDProducer('SiStripRegFEDSelector',
    regSeedLabel = cms.InputTag('hltIsolPixelTrackFilter'),
    rawInputLabel = cms.InputTag('rawDataCollector'),
    delta = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
