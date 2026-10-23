import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationAgainstElectron(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationAgainstElectron',
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag('pfRecoTauProducer'),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    BremCombined_HOP = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(-0.1),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('and'),
      leadTrack = cms.PSet(
        cut = cms.required.double,
        Producer = cms.required.InputTag
      )
    ),
    ApplyCut_BremCombined = cms.bool(False),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(False),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
