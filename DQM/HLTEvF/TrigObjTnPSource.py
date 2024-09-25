import FWCore.ParameterSet.Config as cms

def TrigObjTnPSource(*args, **kwargs):
  mod = cms.EDProducer('TrigObjTnPSource',
    triggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    histColls = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
