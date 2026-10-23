import FWCore.ParameterSet.Config as cms

def LowPtGsfElectronCoreProducer(*args, **kwargs):
  mod = cms.EDProducer('LowPtGsfElectronCoreProducer',
    gsfPfRecTracks = cms.InputTag('lowPtGsfElePfGsfTracks'),
    ctfTracks = cms.InputTag('generalTracks'),
    superClusters = cms.InputTag('lowPtGsfElectronSuperClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
