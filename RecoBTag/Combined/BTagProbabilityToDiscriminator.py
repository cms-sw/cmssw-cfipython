import FWCore.ParameterSet.Config as cms

def BTagProbabilityToDiscriminator(**kwargs):
  mod = cms.EDProducer('BTagProbabilityToDiscriminator',
    discriminators = cms.VPSet(
      cms.PSet(
        denominator = cms.VInputTag(),
        name = cms.string('BvsAll'),
        numerator = cms.VInputTag(
          'pfDeepCSVJetTags:probb',
          'pfDeepCSVJetTags:probbb'
        )
      ),
      cms.PSet(
        denominator = cms.VInputTag(
          'pfDeepCSVJetTags:probc',
          'pfDeepCSVJetTags:probb',
          'pfDeepCSVJetTags:probbb'
        ),
        name = cms.string('CvsB'),
        numerator = cms.VInputTag('pfDeepCSVJetTags:probc')
      ),
      cms.PSet(
        denominator = cms.VInputTag(
          'pfDeepCSVJetTags:probudsg',
          'pfDeepCSVJetTags:probc'
        ),
        name = cms.string('CvsL'),
        numerator = cms.VInputTag('pfDeepCSVJetTags:probc')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
