import FWCore.ParameterSet.Config as cms

muCSCTnPFlatTableProducer = cms.EDProducer('MuCSCTnPFlatTableProducer',
  name = cms.string('cscTnP'),
  muonSrc = cms.InputTag('muons'),
  trackSrc = cms.InputTag('generalTracks'),
  cscSegmentSrc = cms.InputTag('cscSegments'),
  primaryVerticesSrc = cms.InputTag('offlinePrimaryVertices'),
  trigEventSrc = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  trigResultsSrc = cms.InputTag('TriggerResults', '', 'HLT'),
  trigName = cms.string('none'),
  isoTrigName = cms.string('HLT_IsoMu2*'),
  mightGet = cms.optional.untracked.vstring
)
