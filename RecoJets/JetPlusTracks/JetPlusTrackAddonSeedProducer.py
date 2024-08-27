import FWCore.ParameterSet.Config as cms

def JetPlusTrackAddonSeedProducer(**kwargs):
  mod = cms.EDProducer('JetPlusTrackAddonSeedProducer',
    dRcone = cms.double(0.4),
    UsePAT = cms.bool(False),
    srcCaloJets = cms.InputTag('ak4CaloJets'),
    srcTrackJets = cms.InputTag('ak4TrackJets'),
    srcPVs = cms.InputTag('primaryVertex'),
    PFCandidates = cms.InputTag('PFCandidates'),
    towerMaker = cms.InputTag('towerMaker'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
