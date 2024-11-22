import FWCore.ParameterSet.Config as cms

def LowPtGsfElectronSCProducer(*args, **kwargs):
  mod = cms.EDProducer('LowPtGsfElectronSCProducer',
    gsfPfRecTracks = cms.InputTag('lowPtGsfElePfGsfTracks'),
    ecalClusters = cms.InputTag('particleFlowClusterECAL'),
    hcalClusters = cms.InputTag('particleFlowClusterHCAL'),
    MaxDeltaR2 = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
