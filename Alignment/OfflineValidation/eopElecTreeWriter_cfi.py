import FWCore.ParameterSet.Config as cms

eopElecTreeWriter = cms.EDAnalyzer('EopElecTreeWriter',
  src = cms.InputTag('electronGsfTracks'),
  triggerPath = cms.string('HLT_Ele'),
  hltFilter = cms.string('hltDiEle27L1DoubleEGWPTightHcalIsoFilter'),
  debugTriggerSelection = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
