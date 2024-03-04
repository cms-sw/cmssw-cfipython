import FWCore.ParameterSet.Config as cms

def AlCaLowPUHBHEMuonFilter(**kwargs):
  mod = cms.EDFilter('AlCaLowPUHBHEMuonFilter',
    processName = cms.string('HLT'),
    triggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
    muonLabel = cms.InputTag('muons'),
    minimumMuonpT = cms.double(10),
    minimumMuoneta = cms.double(1.305),
    triggers = cms.vstring(
      'HLT_L1DoubleMu',
      'HLT_L1SingleMu'
    ),
    pfIsolationCut = cms.double(0.15),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
