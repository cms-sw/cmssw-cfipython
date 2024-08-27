import FWCore.ParameterSet.Config as cms

def TrigObjTnPSource(**kwargs):
  mod = cms.EDProducer('TrigObjTnPSource',
    triggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    histColls = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
