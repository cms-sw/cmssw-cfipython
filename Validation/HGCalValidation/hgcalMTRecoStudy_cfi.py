import FWCore.ParameterSet.Config as cms

hgcalMTRecoStudy = cms.EDAnalyzer('HGCalMTRecoStudy',
  detectorName = cms.string('HGCalEESensitive'),
  source = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  layerList = cms.string('1'),
  mightGet = cms.optional.untracked.vstring
)
