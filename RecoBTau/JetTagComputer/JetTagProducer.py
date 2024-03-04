import FWCore.ParameterSet.Config as cms

def JetTagProducer(**kwargs):
  mod = cms.EDProducer('JetTagProducer',
    jetTagComputer = cms.string('combinedMVAComputer'),
    tagInfos = cms.VInputTag(
      'impactParameterTagInfos',
      'inclusiveSecondaryVertexFinderTagInfos',
      'softPFMuonsTagInfos',
      'softPFElectronsTagInfos'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
