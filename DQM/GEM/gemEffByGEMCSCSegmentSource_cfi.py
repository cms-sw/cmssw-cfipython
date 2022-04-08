import FWCore.ParameterSet.Config as cms

gemEffByGEMCSCSegmentSource = cms.EDProducer('GEMEffByGEMCSCSegmentSource',
  gemcscSegmentTag = cms.InputTag('gemcscSegments'),
  muonTag = cms.InputTag('muons'),
  useMuon = cms.untracked.bool(False),
  minCSCRecHits = cms.untracked.uint32(6),
  folder = cms.untracked.string('GEM/Efficiency/GEMCSCSegment'),
  logCategory = cms.untracked.string('GEMEffByGEMCSCSegmentSource'),
  mightGet = cms.optional.untracked.vstring
)
