import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationByLeadingObjectPtCut(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationByLeadingObjectPtCut',
    MinPtLeadingObject = cms.double(5),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(False),
    PFTauProducer = cms.InputTag('pfRecoTauProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
