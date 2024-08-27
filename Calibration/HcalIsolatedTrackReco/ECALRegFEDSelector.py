import FWCore.ParameterSet.Config as cms

def ECALRegFEDSelector(**kwargs):
  mod = cms.EDProducer('ECALRegFEDSelector',
    regSeedLabel = cms.InputTag('hltPixelIsolTrackFilter'),
    rawInputLabel = cms.InputTag('rawDataCollector'),
    delta = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
