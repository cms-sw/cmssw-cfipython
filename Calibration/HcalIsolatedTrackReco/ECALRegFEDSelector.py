import FWCore.ParameterSet.Config as cms

def ECALRegFEDSelector(*args, **kwargs):
  mod = cms.EDProducer('ECALRegFEDSelector',
    regSeedLabel = cms.InputTag('hltPixelIsolTrackFilter'),
    rawInputLabel = cms.InputTag('rawDataCollector'),
    delta = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
