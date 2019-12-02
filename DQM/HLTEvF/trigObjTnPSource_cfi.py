import FWCore.ParameterSet.Config as cms

trigObjTnPSource = cms.EDAnalyzer('TrigObjTnPSource',
  triggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  histColls = cms.VPSet(
  ),
  mightGet = cms.optional.untracked.vstring
)
