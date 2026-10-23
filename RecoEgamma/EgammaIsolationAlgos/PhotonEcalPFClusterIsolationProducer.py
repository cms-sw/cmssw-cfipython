import FWCore.ParameterSet.Config as cms

def PhotonEcalPFClusterIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('PhotonEcalPFClusterIsolationProducer',
    candidateProducer = cms.InputTag('gedGsfElectrons'),
    pfClusterProducer = cms.InputTag('particleFlowClusterECAL'),
    drMax = cms.double(0.3),
    drVetoBarrel = cms.double(0),
    drVetoEndcap = cms.double(0),
    etaStripBarrel = cms.double(0),
    etaStripEndcap = cms.double(0),
    energyBarrel = cms.double(0),
    energyEndcap = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
