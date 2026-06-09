import FWCore.ParameterSet.Config as cms

def JetTagProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
