import FWCore.ParameterSet.Config as cms

def GEDGsfElectronCoreProducer(*args, **kwargs):
  mod = cms.EDProducer('GEDGsfElectronCoreProducer',
    ctfTracks = cms.InputTag('generalTracks'),
    GEDEMUnbiased = cms.InputTag('particleFlowEGamma'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
