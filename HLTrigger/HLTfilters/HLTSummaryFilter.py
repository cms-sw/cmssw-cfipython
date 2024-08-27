import FWCore.ParameterSet.Config as cms

def HLTSummaryFilter(**kwargs):
  mod = cms.EDFilter('HLTSummaryFilter',
    saveTags = cms.bool(True),
    summary = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    member = cms.InputTag('hlt1jet30', '', 'HLT'),
    cut = cms.string('pt>80'),
    minN = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
