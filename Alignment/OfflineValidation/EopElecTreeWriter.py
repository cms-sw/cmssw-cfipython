import FWCore.ParameterSet.Config as cms

def EopElecTreeWriter(**kwargs):
  mod = cms.EDAnalyzer('EopElecTreeWriter',
    src = cms.InputTag('electronGsfTracks'),
    triggerPath = cms.string('HLT_Ele'),
    hltFilter = cms.string('hltDiEle27L1DoubleEGWPTightHcalIsoFilter'),
    debugTriggerSelection = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
