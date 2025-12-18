import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationAgainstElectron2(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationAgainstElectron2',
    rejectTausInEcalCrack = cms.bool(False),
    PFTauProducer = cms.InputTag('pfRecoTauProducer'),
    applyCut_GammaEnFrac = cms.bool(True),
    applyCut_HLTSpecific = cms.bool(True),
    GammaEnFrac_barrel_max = cms.double(0.15),
    keepTausInEcalCrack = cms.bool(True),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('and'),
      leadTrack = cms.PSet(
        cut = cms.required.double,
        Producer = cms.required.InputTag
      )
    ),
    applyCut_GammaPhiMom = cms.bool(False),
    GammaPhiMom_endcap_max = cms.double(1.5),
    GammaPhiMom_barrel_max = cms.double(1.5),
    applyCut_leadPFChargedHadrEoP = cms.bool(True),
    LeadPFChargedHadrEoP_barrel_max = cms.double(1.01),
    GammaEtaMom_endcap_max = cms.double(1.5),
    GammaEtaMom_barrel_max = cms.double(1.5),
    Hcal3x3OverPLead_endcap_max = cms.double(0.1),
    LeadPFChargedHadrEoP_barrel_min = cms.double(0.99),
    LeadPFChargedHadrEoP_endcap_max2 = cms.double(1.01),
    LeadPFChargedHadrEoP_endcap_min1 = cms.double(0.7),
    LeadPFChargedHadrEoP_endcap_min2 = cms.double(0.99),
    LeadPFChargedHadrEoP_endcap_max1 = cms.double(1.3),
    verbosity = cms.int32(0),
    GammaEnFrac_endcap_max = cms.double(0.2),
    applyCut_hcal3x3OverPLead = cms.bool(True),
    applyCut_GammaEtaMom = cms.bool(False),
    etaCracks = cms.vstring(
      '0.0:0.018',
      '0.423:0.461',
      '0.770:0.806',
      '1.127:1.163',
      '1.460:1.558'
    ),
    Hcal3x3OverPLead_barrel_max = cms.double(0.2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
