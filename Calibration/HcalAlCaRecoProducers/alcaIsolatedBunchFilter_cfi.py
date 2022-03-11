import FWCore.ParameterSet.Config as cms

alcaIsolatedBunchFilter = cms.EDFilter('AlCaIsolatedBunchFilter',
  triggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
  processName = cms.string('HLT'),
  triggerIsoBunch = cms.vstring('HLT_ZeroBias_IsolatedBunches'),
  triggerJet = cms.vstring(
    'HLT_AK8PFJet',
    'HLT_AK8PFHT',
    'HLT_CaloJet',
    'HLT_HT',
    'HLT_JetE',
    'HLT_PFHT',
    'HLT_DiPFJet',
    'HLT_PFJet',
    'HLT_DiCentralPFJet',
    'HLT_QuadPFJet',
    'HLT_L1_TripleJet_VBF',
    'HLT_QuadJet',
    'HLT_DoubleJet',
    'HLT_AK8DiPFJet',
    'HLT_AK4CaloJet',
    'HLT_AK4PFJet'
  ),
  mightGet = cms.optional.untracked.vstring
)
