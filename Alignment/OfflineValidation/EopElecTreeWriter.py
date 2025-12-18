import FWCore.ParameterSet.Config as cms

def EopElecTreeWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('EopElecTreeWriter',
    src = cms.InputTag('electronGsfTracks'),
    triggerPath = cms.string('HLT_Ele'),
    hltFilter = cms.string('hltDiEle27L1DoubleEGWPTightHcalIsoFilter'),
    debugTriggerSelection = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
