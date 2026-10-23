import FWCore.ParameterSet.Config as cms

def HLTSummaryFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTSummaryFilter',
    saveTags = cms.bool(True),
    summary = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    member = cms.InputTag('hlt1jet30', '', 'HLT'),
    cut = cms.string('pt>80'),
    minN = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
