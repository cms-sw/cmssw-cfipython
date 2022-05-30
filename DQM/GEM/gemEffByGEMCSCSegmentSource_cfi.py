import FWCore.ParameterSet.Config as cms

gemEffByGEMCSCSegmentSource = cms.EDProducer('GEMEffByGEMCSCSegmentSource',
  ohStatusTag = cms.untracked.InputTag('muonGEMDigis', 'OHStatus'),
  vfatStatusTag = cms.untracked.InputTag('muonGEMDigis', 'VFATStatus'),
  monitorGE11 = cms.untracked.bool(True),
  monitorGE21 = cms.untracked.bool(False),
  monitorGE0 = cms.untracked.bool(False),
  maskChamberWithError = cms.untracked.bool(False),
  logCategory = cms.untracked.string('GEMEffByGEMCSCSegmentSource'),
  gemcscSegmentTag = cms.untracked.InputTag('gemcscSegments'),
  muonTag = cms.untracked.InputTag('muons'),
  minCSCRecHits = cms.untracked.int32(6),
  useMuonSegment = cms.untracked.bool(False),
  modeDev = cms.untracked.bool(False),
  folder = cms.untracked.string('GEM/Efficiency/GEMCSCSegment'),
  mightGet = cms.optional.untracked.vstring
)
