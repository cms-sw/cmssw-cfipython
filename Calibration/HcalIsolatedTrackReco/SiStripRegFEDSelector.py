import FWCore.ParameterSet.Config as cms

def SiStripRegFEDSelector(**kwargs):
  mod = cms.EDProducer('SiStripRegFEDSelector',
    regSeedLabel = cms.InputTag('hltIsolPixelTrackFilter'),
    rawInputLabel = cms.InputTag('rawDataCollector'),
    delta = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
