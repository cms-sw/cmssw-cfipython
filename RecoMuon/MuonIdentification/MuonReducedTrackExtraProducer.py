import FWCore.ParameterSet.Config as cms

def MuonReducedTrackExtraProducer(**kwargs):
  mod = cms.EDProducer('MuonReducedTrackExtraProducer',
    muonTag = cms.InputTag('muons'),
    trackExtraTags = cms.VInputTag(
      'generalTracks',
      'globalMuons',
      'tevMuons:firstHit',
      'tevMuons:picky',
      'tevMuons:dyt'
    ),
    trackExtraAssocs = cms.VInputTag(),
    pixelClusterTag = cms.InputTag('siPixelClusters'),
    stripClusterTag = cms.InputTag('siStripClusters'),
    cut = cms.string('pt > 3.0'),
    outputClusters = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
