import FWCore.ParameterSet.Config as cms

def SUSY_HLT_Razor(*args, **kwargs):
  mod = cms.EDProducer('SUSY_HLT_Razor',
    jetCollection = cms.InputTag('ak4PFJetsCHS'),
    CaloFilter = cms.InputTag('hltRsqMR200Rsq0p01MR100Calo', '', 'HLT'),
    METCollection = cms.InputTag('pfMet'),
    hemispheres = cms.InputTag('hemispheres'),
    TriggerPath = cms.string('HLT_RsqMR300_Rsq0p09_MR200_v'),
    TriggerFilter = cms.InputTag('hltRsqMR300Rsq0p09MR200', '', 'HLT'),
    TriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    trigSummary = cms.InputTag('hltTriggerSummaryAOD'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
